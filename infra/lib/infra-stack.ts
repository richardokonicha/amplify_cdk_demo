import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import { CfnApp, CfnBranch, CfnDomain } from 'aws-cdk-lib/aws-amplify';
import { CfnIdentityPool, UserPool, UserPoolClient } from "aws-cdk-lib/aws-cognito"

export class InfraStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);


    // CREATE COGNITO USER POOL AND IDENTITY POOL 
    const userPool = new UserPool(this, "AmplifyCDKUserPool", {
      selfSignUpEnabled: true, // Allow users to sign up
      autoVerify: { email: true }, // Verify email addresses by sending a verification code
      signInAliases: { email: true }, // Set email as an alias
    });

    const userPoolClient = new UserPoolClient(this, "AmplifyCDKUserPoolClient", {
      userPool,
      generateSecret: false, // Don't need to generate secret for web app running on browsers
    });

    const identityPool = new CfnIdentityPool(this, "AmplifyCDKIdentityPool", {
      allowUnauthenticatedIdentities: true,
      cognitoIdentityProviders: [{
        clientId: userPoolClient.userPoolClientId,
        providerName: userPool.userPoolProviderName,
      }],
    });
    // 

    const app = new CfnApp(this, 'DemoApp', {
      name: 'amplify_cdk_demo',
      repository: 'https://github.com/richardokonicha/amplify_cdk_demo',
      accessToken: 'ghp_KSsrz2C3e5UfLY9cMDE8SHzXn********',

      environmentVariables: [
        {
          name: "IDENTITY_POOL_ID",
          value: identityPool.ref,
        },
        {
          name: "USER_POOL_ID",
          value: userPool.userPoolId,
        },
        {
          name: "USER_POOL_CLIENT_ID",
          value: userPoolClient.userPoolClientId,
        },
        {
          name: "REGION",
          value: this.region,
        },
      ],


    });

    new CfnBranch(this, 'DemoBranch', {
      appId: app.attrAppId,
      branchName: 'main', // you can put any branch here (careful, it will listen to changes on this branch),

      environmentVariables: [
        {
          name: "IDENTITY_POOL_ID",
          value: identityPool.ref,
        },
        {
          name: "USER_POOL_ID",
          value: userPool.userPoolId,
        },
        {
          name: "USER_POOL_CLIENT_ID",
          value: userPoolClient.userPoolClientId,
        },
        {
          name: "REGION",
          value: this.region,
        },
      ],

    });

  }
}

// for when we not usng modules
// const app = new cdk.App();
// new InfraStack(app, 'demo');
// app.synth();
