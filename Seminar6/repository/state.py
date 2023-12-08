def add_state(states,state):
    states.append(state)

def get_current_state(states):
    return states[-1]

def set_initial_state(states,word):
    states.append((0,2,[0,len(word)-1]))