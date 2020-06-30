import request from '@/utils/request'

export function getUserInfo() {
  return request({
    url: '/user/profile',
    method: 'get'
  })
}

export function updateUserInfo(data) {
  return request({
    url: '/user/profile',
    method: 'put',
    data
  })
}

export function getAllUsers() {
  return request({
    url: 'admin/users/',
    method: 'get'
  })
}
