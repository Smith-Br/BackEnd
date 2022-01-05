<Picker
    prompt={'Order status'}
    selectedValue={status}
    onValuehange={onUpdateStatus}>
    {
        STATUSES.map(status => {
            if (status !== 'complete') return
            return <Text>{status}</Text>
        })
    }
</Picker>