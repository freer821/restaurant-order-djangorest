import request from '@/utils/request'

export function getUserInfo() {
  return request({
    url: '/api/user/profile',
    method: 'get'
  })
}

export function updateUserInfo(data) {
  return request({
    url: '/api/user/profile',
    method: 'put',
    data
  })
}

export function getAllUsers() {
  return request({
    url: 'api/admin/users/',
    method: 'get'
  })
}

export function fetchUserListAdmin(params) {
  return request({
    url: 'api/admin/users/',
    method: 'get',
    params
  })
}

export function fetchDashboadInfo() {
  return request({
    url: 'api/dashboard',
    method: 'get'
  })
}
