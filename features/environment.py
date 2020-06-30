from steps.actionwords import Actionwords

def before_scenario(context, scenario):
    context.actionwords = Actionwords()
