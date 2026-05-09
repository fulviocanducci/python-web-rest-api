def apply_patch(obj, data):
    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(obj, field, value)
