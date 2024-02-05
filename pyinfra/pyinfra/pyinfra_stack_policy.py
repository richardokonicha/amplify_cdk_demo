from aws_cdk import aws_iam as iam, aws_amplify as amplify, Stack
from aws_cdk.aws_amplify import CfnApp, CfnBranch
from aws_cdk.aws_cognito import UserPool, UserPoolClient, CfnIdentityPool
import aws_cdk.aws_cognito as cognito
from constructs import Construct

class PyinfraStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        
        # Create a Cognito User Pool
        user_pool = UserPool(self, 'MyUserPool',
                             user_pool_name='MyUserPool',
                             self_sign_up_enabled=True,
                            #  sign_in_aliases=True
                            #  auto_verify={'email': True},
                             )
        user_pool_client = UserPoolClient(self, 'MyUserPoolClient', user_pool=user_pool, generate_secret=False)
        
        identity_pool = cognito.CfnIdentityPool( self, 'newIdentityPool', {
            'allowUnauthenticatedIdentities': True,
            'cognitoIdentityProviders': [{
                'clientId': user_pool_client.user_pool_client_id,
                'providerName': user_pool.user_pool_provider_name
            }]
        })
        
        # # Create an Amplify App
        amplify_app = CfnApp(self, 'NewDemoApp',
                             name='newamplify_cdk_demo',
                             repository='https://github.com/richardokonicha/amplify_cdk_demo',
                             access_token='ghp_KSsrz2C3e5UfLY9cMDE8SHzXna******',
                             iam_service_role="arn:aws:iam::70932312****5:role/amplify_test",
                             
                             environment_variables={
                                  'REGION': self.region,
                                  'IDENTITY_POOL_ID': identity_pool.ref,
                                  'USER_POOL_ID': user_pool.user_pool_id,
                                  'USER_POOL_CLIENT_ID': user_pool_client.user_pool_client_id,
                                  
                                  'AMPLIFY_USERPOOL_ID': user_pool.user_pool_id,
                                  'AMPLIFY_WEBCLIENT_ID': UserPoolClient(self, 'MyUserPoolClient', user_pool=user_pool).user_pool_client_id,
                             }
                             # https://github.com/apps/aws-amplify-eu-north-1/installations/new - to install amplify app
                             )

        # Create an IAM service role for the Amplify App
        # amplify_app_role = iam.Role(self, 'AmplifyAppRole',
        #                             assumed_by=iam.ServicePrincipal('amplify.amazonaws.com'))
        # amplify_app.iam_service_role = "arn:aws:iam::709323121715:role/amplify_test"
        # Attach policies to the service role
        # amplify_app_role.add_managed_policy(iam.ManagedPolicy.from_aws_managed_policy_name('AdministratorAccess-Amplify'))

        # Set the service role for the Amplify App
        # amplify_app.iam_service_role = amplify_app_role.role_arn

        # Create an Amplify Branch
        amplify_branch = CfnBranch(self, 'DemoBranch',
                                   app_id=amplify_app.attr_app_id,
                                   branch_name='dev')

 

        # Add authentication configuration to the Amplify Branch
        # eu-north-1_kq6uXBEXL
        # amplify_branch.add_override('authConfiguration', {
        #     'userPoolId': user_pool.user_pool_id,
        #     'userPoolWebClientId': UserPoolClient(self, 'MyUserPoolClient', user_pool=user_pool).user_pool_client_id
        # })

        # amplify_branch.add_override('authConfiguration', {
        #     'userPoolId': "eu-north-1_kq6uXBEXL",
        #     'userPoolWebClientId': UserPoolClient(self, 'MyUserPoolClient', user_pool=user_pool).user_pool_client_id
        # })

        # Add environment variables to the Amplify App
        # amplify_app.add_environment(name="AMPLIFY_USERPOOL_ID", value=user_pool.user_pool_id)
        # amplify_app.add_environment(name="AMPLIFY_WEBCLIENT_ID", value=UserPoolClient(self, 'MyUserPoolClient', user_pool=user_pool).user_pool_client_id)
        # amplify_app.add_environment(name="AMPLIFY_NATIVECLIENT_ID", value=UserPoolClient(self, 'MyUserPoolClient', user_pool=user_pool).user_pool_client_id)
