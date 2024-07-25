import numpy as np

def pull_once(prob):
    '''
    Pull once

    Output:
        - result: string "N", "P" representing "no prize" "prize"
    '''

    result = np.random.choice(['P', 'N'], p = [prob, 1 - prob])

    return result


def implement_experiment(prob, N, n):
    '''
    Pull for n times

    Output: 
        - result: an array of "P", "NFP", "FP"
    '''
    result = []
    T = 0
    lastprize = ""

    for i in range(n):
        if T == N - 1:
           pull = 'P'
        else:
            pull = pull_once(prob)

        if pull == 'P':
            if lastprize == 'NFP':
                pull = np.str_('FP')
            else:
                pull = np.random.choice(['FP','NFP'],p = [0.5, 0.5])
            
            lastprize = pull
            T = 0
        else:
            T += 1

        result.append(pull)

    return result


def pull_until_P(prob, N):
    result = []
    T = 0
    lastprize = ""
    pullTime = 0

    while True:
        if T == N - 1:
           pull = 'P'
        else:
            pull = pull_once(prob)

        if pull == 'P':
            if lastprize == 'NFP':
                pull = np.str_('FP')
            else:
                pull = np.random.choice(['FP','NFP'],p = [0.5, 0.5])
            
            lastprize = pull
            T = 0
            pullTime += 1
            result.append(pull)
            break
        else:
            T += 1

        pullTime += 1
        result.append(pull)
    
    d = {
        "pullTime":pullTime,
        "result":result
    }

    return d

def pull_until_FP(prob, N):
    result = []
    T = 0
    lastprize = ""
    pullTime = 0

    while True:
        if T == N - 1:
           pull = 'P'
        else:
            pull = pull_once(prob)

        if pull == 'P':
            if lastprize == 'NFP':
                pull = np.str_('FP')
            else:
                pull = np.random.choice(['FP','NFP'],p = [0.5, 0.5])
            
            lastprize = pull
            T = 0
            pullTime += 1

            if pull == 'FP':
                pullTime += 1
                result.append(pull)
                break
        else:
            T += 1
            
        pullTime += 1
        result.append(pull)
    
    d = {
        "pullTime":pullTime,
        "result":result
    }

    return d

def expected_pullTime_until_P(prob, N, n):

    avg = 0

    for i in range(n):
        d = pull_until_P(prob, N)
        pullTime = d['pullTime']
        avg += pullTime

    avg /= n  
    return avg

def expected_pullTime_until_FP(prob, N, n):

    avg = 0

    for i in range(n):
        d = pull_until_FP(prob, N)
        pullTime = d['pullTime']
        avg += pullTime

    avg /= n  
    return avg

def conduct_experiment(prob, N, n):
    until_P_avg = expected_pullTime_until_P(prob, N, n)
    until_FP_avg = expected_pullTime_until_FP(prob, N, n)

    d = {
        'ET':until_P_avg,
        "ETstar":until_FP_avg
    }

    return d 