#!/usr/bin/env python3
import os
import aws_cdk.core as cdk
from stacks.app_stack import BookManagementAppStack

app = cdk.App()
BookManagementAppStack(app, "BookManagementAppStack")
app.synth()