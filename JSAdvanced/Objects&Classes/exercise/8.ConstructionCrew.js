function workerModification(params) {
    if (!params['dizziness']) return params

    params['levelOfHydrated'] += (0.1 * params['weight']) * params['experience'], params['dizziness'] = false
    return params
}
