import boto3
project = "upb-cf"

cf = boto3.client('cloudformation')

with open('template.yaml', 'r') as file:
    template = file.read()

create_stack_response = cf.create_stack(
    StackName=project,
    TemplateBody=template
)

# create_stack_response = cf.create_change_set(
#     StackName=project,
#     TemplateBody=template,
#     ChangeSetName="hiworld"
# )

# create_stack_response = cf.delete_stack(
#     StackName=project
# )

# create_stack_response = cf.update_stack(
#     StackName=project,
#     TemplateBody=template
# )

print(create_stack_response)
