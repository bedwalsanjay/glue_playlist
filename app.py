#!/usr/bin/env python3
import aws_cdk as cdk
from src import config

from src.glue_stack import GlueStackClass

app = cdk.App()

# env = cdk.Environment(account=config.ACCOUNT_ID, region=config.REGION)

glue_cdk_stack = GlueStackClass(
    scope=app,
    construct_id="cdk-glue-demo",
    account_id=config.ACCOUNT_ID,
    region=config.REGION,
    # env=["dev"],
    # synthesizer=stack_synthesizer,
)

app.synth()
