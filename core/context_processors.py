def load_env_variables(request):
    
    # Validate if the user is an admin
    user_root = request.user.is_superuser if request.user.is_authenticated else False
    user_group = request.user.groups.all() if request.user.is_authenticated else None
    user_group_name = user_group[0].name if user_group else None
        
    return {
        'USER_ROOT': user_root,
        'USER_GROUP': user_group_name,
    }