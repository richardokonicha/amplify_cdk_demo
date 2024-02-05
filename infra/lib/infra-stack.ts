import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import { CfnApp, CfnBranch, CfnDomain } from 'aws-cdk-lib/aws-amplify';

export class InfraStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const app = new CfnApp(this, 'DemoApp', {
      name: 'amplify_cdk_demo',
      repository: 'https://github.com/richardokonicha/amplify_cdk_demo',
      accessToken: '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'
      // https://github.com/apps/aws-amplify-eu-north-1/installations/new - to install amplify app
    });

    new CfnBranch(this, 'DemoBranch', {
      appId: app.attrAppId,
      branchName: 'main' // you can put any branch here (careful, it will listen to changes on this branch)
    });

  }
}

// for when we not usng modules
// const app = new cdk.App();
// new InfraStack(app, 'demo');
// app.synth();
