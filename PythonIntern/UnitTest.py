from KodPython import verify_aws_iam_role_policy
import unittest

class TestVerifyAwsIamRolePolicy(unittest.TestCase):
    def test_verify_aws_iam_role_policy(self):
        # Test case: 'Resource' field does not contain a single asterisk
        data1 = {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Effect": "Allow",
                    "Action": "s3:ListBucket",
                    "Resource": "arn:aws:s3:::example_bucket"
                }
            ]
        }
        self.assertTrue(verify_aws_iam_role_policy(data1))

        # Test case: 'Resource' field contains a single asterisk
        data2 = {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Effect": "Allow",
                    "Action": "s3:ListBucket",
                    "Resource": "*"
                }
            ]
        }
        self.assertFalse(verify_aws_iam_role_policy(data2))

if __name__ == '__main__':
    unittest.main()