#!/usr/bin/python3
import getopt, sys

argument_list = sys.argv[1:]
short_options = "ho:v"
long_options = ["create", "delete", "update", "set"]

try:
    arguments, values = getopt.getopt(argument_list, short_options, long_options)
    command = arguments[0][0].split('--')[1]
except getopt.error as err:
    print (str(err))
    sys.exit(2)

###############################################################################
import boto3

cf = boto3.client('cloudformation')

with open('template.yaml', 'r') as file:
    template = file.read()

project = "upb-cf"

if command == "create":
    create_stack_response = cf.create_stack(
        StackName=project,
        TemplateBody=template
    )
    print(create_stack_response)

elif command == "update":
    update_stack_response = cf.update_stack(
        StackName=project,
        TemplateBody=template
    )
    print(update_stack_response)

elif command == "delete":
    delete_stack_response = cf.delete_stack(
        StackName=project
    )

elif command == "set":
    change_set_response = cf.create_change_set(
        StackName=project,
        TemplateBody=template,
        ChangeSetName="uniquestring"
    )
    print(change_set_response)
    
else:
    print("No command recognized")


