#!/usr/bin/env python3
import os
import aws_cdk as core
from stacks.app_stack import BookManagementAppStack

app = core.App()
BookManagementAppStack(app, "BookManagementAppStack")
app.synth()