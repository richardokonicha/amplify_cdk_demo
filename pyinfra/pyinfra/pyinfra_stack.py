# from aws_cdk import (
#     # Duration,
#     Stack,
#     # aws_sqs as sqs,
# )
# from constructs import Construct
# # from aws_cdk import Stack, App, aws_s3 as s3
# # from aws_cdk import core
# from aws_cdk.aws_amplify import CfnApp, CfnBranch

# class PyinfraStack(Stack):
#     def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
#         super().__init__(scope, construct_id, **kwargs)
#         # The code that defines your stack goes here
    
#         app = CfnApp(self, 'DemoApp',
#                      name='amplify_cdk_demo',
#                      repository='https://github.com/richardokonicha/amplify_cdk_demo',
#                      access_token='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'
#                      # https://github.com/apps/aws-amplify-eu-north-1/installations/new - to install amplify app
#                      )

#         CfnBranch(self, 'DemoBranch',
#                   app_id=app.attr_app_id,
#                   branch_name='main'  # you can put any branch here (careful, it will listen to changes on this branch)
#                   )


# # app = App()
# # PyinfraStack(app, "PyinfraStack")
# # app.synth()

