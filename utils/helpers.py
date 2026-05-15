history=[]

MAX_HISTORY=10

def manage_history(role,content):

    history.append({"role":role,
                    "content":content})
    
    if len(history)>MAX_HISTORY:
        history.pop(0)

    return history    