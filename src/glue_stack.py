from aws_cdk import (
    Stack,
    aws_iam as iam,
    aws_glue as glue,
    aws_s3 as s3,
    aws_s3_assets as s3_assets,
)

from constructs import Construct
import src.config as config
import aws_cdk as cdk


class GlueStackClass(Stack):
    def __init__(
        self,
        scope: Construct,
        construct_id: str,
        account_id: str,
        region: str,
        **kwargs,
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create the IAM Role for the Glue Job
        demo_glue_role = iam.Role(
            self,
            "demo--glue-role",
            assumed_by=iam.ServicePrincipal("glue.amazonaws.com"),
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name(
                    "service-role/AWSGlueServiceRole"
                ),
                iam.ManagedPolicy.from_aws_managed_policy_name("AmazonS3FullAccess"),
                iam.ManagedPolicy.from_aws_managed_policy_name(
                    "CloudWatchLogsFullAccess"
                ),
            ],
        )

        demo_glue_role.attach_inline_policy(
            iam.Policy(
                self,
                "glue-role-kms-inline-policy",
                policy_name="glue-role-kms-inline-policy",
                statements=[
                    iam.PolicyStatement(
                        actions=[
                            "kms:Decrypt",
                            "kms:DescribeKey",
                            "kms:Encrypt",
                            "kms:GenerateDataKey",
                        ],
                        resources=["*"],
                    )
                ],
            )
        )

        # # Create glue Security Configuration
        # glue.CfnSecurityConfiguration(
        #     self,
        #     "glue_sec_config",
        #     encryption_configuration=glue.CfnSecurityConfiguration.EncryptionConfigurationProperty(
        #         s3_encryptions=[
        #             glue.CfnSecurityConfiguration.S3EncryptionProperty(
        #                 s3_encryption_mode="SSE-S3"
        #             )
        #         ]
        #     ),
        #     name=config.GLUE_SECURITY_CONFIG,
        # )

        # add glue script location
        glue_script_loc = s3_assets.Asset(
            self,
            "s3-assets--load-s3-rds",
            path="src/glue/glue_python_shell_command_line_args_right_way.py",
        )

        # Define a Glue job (Python shell)
        glue_job = glue.CfnJob(
            self,
            "GlueJob",
            name="glue-demo-1",
            role=demo_glue_role.role_arn,
            command={
                "name": "pythonshell",
                "scriptLocation": glue_script_loc.s3_object_url,
                "pythonVersion": "3.9",
            },
            default_arguments={
                "--additional-python-modules": "xlrd,cursor,pymssql",
                "--enable-glue-datacatalog": "true",
            },
            max_retries=0,
            timeout=3,
            # security_configuration=config.GLUE_SECURITY_CONFIG,
        )


        # Output the Glue job name
        cdk.CfnOutput(
            self, "GlueJobName", value=glue_job.name
        )
