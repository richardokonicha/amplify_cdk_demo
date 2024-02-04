import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import { CfnApp, CfnBranch, CfnDomain } from 'aws-cdk-lib/aws-amplify';

// import { App } from 'aws-cdk-lib/aws-amplify';
// import { AppProps } from 'aws-cdk-lib/aws-amplify';
// import { CfnApp } from 'aws-cdk-lib/aws-amplify';
// import * as sqs from 'aws-cdk-lib/aws-sqs';

export class InfraStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // The code that defines your stack goes here

    // example resource
    // const queue = new sqs.Queue(this, 'InfraQueue', {
    //   visibilityTimeout: cdk.Duration.seconds(300)
    // });

    const amplifyDemo = new CfnApp(this, 'DemoAmplify', {
      name: 'amplify_cdk_demo',
      repository: 'https://github.com/richardokonicha/amplify_cdk_demo.git',
      oauthToken: 'ghp_sometokeen '
      // oauthToken: cdk.SecretValue.secretsManager('github-token')
    });

    new CfnBranch(this, 'MasterBranch', {
      appId: amplifyDemo.attrAppId,
      branchName: 'main' // you can put any branch here (careful, it will listen to changes on this branch)
    });
  }
}


// for when we not usng modules
// const app = new cdk.App();
// new InfraStack(app, 'demo');
// app.synth();