from aws_cdk import aws_iam as iam, Stack
from aws_cdk.aws_amplify import CfnApp, CfnBranch
from aws_cdk.aws_cognito import UserPool, UserPoolClient
from constructs import Construct

class PyinfraStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        amplify_app = CfnApp(self, 'DemoApp',
                             name='amplify_cdk_demo',
                             repository='https://github.com/richardokonicha/amplify_cdk_demo',
                             access_token='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'
                             # https://github.com/apps/aws-amplify-eu-north-1/installations/new - to install amplify app
                             )

        amplify_branch = CfnBranch(self, 'DemoBranch',
                                   app_id=amplify_app.attr_app_id,
                                   branch_name='dev')
        

        # amplify_app.grant_principal.add_managed_policy(iam.ManagedPolicy.from_aws_managed_policy_name('AdministratorAccess-Amplify'))

        print(f"amplify_app.iam_service_role: {amplify_app.iam_service_role}")

        amplify_app_role = iam.Role.from_role_arn(self, "AmplifyAppRole", f"arn:aws:iam::{self.account}:role/{amplify_app.iam_service_role}")

        # Add the 'AdministratorAccess-Amplify' managed policy to the role
        amplify_app_role.add_managed_policy(iam.ManagedPolicy.from_aws_managed_policy_name('AdministratorAccess-Amplify'))


        # Create a user pool  
        user_pool = UserPool(self, 'MyUserPool',
                             user_pool_name='MyUserPool',
                             self_sign_up_enabled=True,
                             auto_verify={'email': True})

        
        
        # user_pool = UserPool.from_user_pool_id(
        #     self, 'AmplifyTestUserPool',
        #     user_pool_id='us-east-1_e7AbW7pQF'
        # )

        amplify_branch.add_override('authConfiguration', {
            'userPoolId': user_pool.user_pool_id,
            'userPoolWebClientId': UserPoolClient(self, 'MyUserPoolClient', user_pool=user_pool).user_pool_client_id
        })
        
        
