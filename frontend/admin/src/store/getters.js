const getters = {
  sidebar: state => state.app.sidebar,
  language: state => state.app.language,
  size: state => state.app.size,
  device: state => state.app.device,
  visitedViews: state => state.tagsView.visitedViews,
  cachedViews: state => state.tagsView.cachedViews,
  token: state => state.user.token,
  avatar: state => state.user.avatar,
  username: state => state.user.username,
  is_admin: state => state.user.is_admin,
  profile: state => state.user.profile,
  permission_routers: state => state.permission.routers,
  addRouters: state => state.permission.addRouters,
  current_user: state => state.admin.current_user,
  all_users: state => state.admin.all_users
}
export default getters
