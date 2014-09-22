from api import app, db
from api.models import Snippet
import unittest
import json


class APIv1Test(unittest.TestCase):
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()
        db.create_all()
        self.load_data()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def load_data(self):
        snippet = Snippet(title="Uploading a file to S3 using Boto",
                          language="python",
                          code="""
                            import cStringIO
                            from boto.s3.connection import S3Connection
                            from boto.s3.key import Key


                            def s3upload(filename, extension, file):
                                conn = S3Connection('AWS_ACCESS_KEY', 'AWS_SECRET_KEY')
                                k = Key(conn.get_bucket('<bucket name>'))
                                k.key = filename
                                k.set_metadata("Content-Type", file.mimetype)
                                fp = cStringIO.StringIO(file.read())
                                k.set_contents_from_file(fp)
                                k.set_acl("public-read")
                                fp.close()
                                return "https://s3.amazonaws.com/<bucket name>/{}.{}".format(filename, extension)
                          """)

        self.snippet1 = snippet
        db.session.add(snippet)
        db.session.commit()

    def test_index(self):
        res = self.app.get('/v1/meta')
        self.assertEqual(res.status_code, 200)

    def test_get_all_snippets(self):
        res = self.app.get('/v1/snippets')
        self.assertEqual(res.status_code, 200)
        data = json.loads(res.data)
        snippets = data['snippets']
        self.assertEqual(len(snippets), 1)
        self.assertEqual(snippets[0]['title'], self.snippet1.title)
        self.assertEqual(snippets[0]['code'], self.snippet1.code)

    def test_submit_snippet(self):
        data = {
            "title": "Doing a push segue using StoryBoard instance instead of the prepareForSegue method",
            "snippet": """
                UIStoryboard * myStoryboard = [UIStoryboard storyboardWithName:@"Main" bundle:nil];
                DestinationViewController *dVC = [myStoryboard instantiateViewControllerWithIdentifier:@"storyboard_id_for_dVC"];
                [self.navigationController pushViewController:urlVC animated:YES];
            """,
            "language": "objective-c"
        }
        res = self.app.post('/v1/snippets',
                            data=json.dumps(data),
                            content_type='application/json')
        self.assertEqual(res.status_code, 201)
        d = json.loads(res.data)
        self.assertIn('id', d.keys())
        snippet = Snippet.query.get(d['id'])
        self.assertEqual(snippet.title, data['title'])
        self.assertEqual(snippet.code, data['snippet'])
        self.assertEqual(snippet.language, data['language'])
