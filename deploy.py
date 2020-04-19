#!/usr/bin/python3
import getopt, sys

argument_list = sys.argv[1:]
short_options = "cdus"
long_options = ["create", "delete", "update", "set"]

try:
    arguments, values = getopt.getopt(argument_list, short_options, long_options)
    command = arguments[0][0]
except getopt.error as err:
    print (str(err))
    sys.exit(2)

###############################################################################
import boto3

cf = boto3.client('cloudformation')

with open('template.yaml', 'r') as file:
    template = file.read()

project = "upb-cf3"

if command in ("--create", "-c"):

    create_stack_response = cf.create_stack(
        StackName=project,
        TemplateBody=template
    )
    print(create_stack_response)

elif command in ("--update", "-u"):

    update_stack_response = cf.update_stack(
        StackName=project,
        TemplateBody=template
    )
    print(update_stack_response)

elif command in ("--delete", "-d"):

    delete_stack_response = cf.delete_stack(
        StackName=project
    )
    print(delete_stack_response)

elif command in ("--set", "-s"):

    change_set_response = cf.create_change_set(
        StackName=project,
        TemplateBody=template,
        ChangeSetName="uniquestring"
    )
    print(change_set_response)

else:
    print("No command recognized")


