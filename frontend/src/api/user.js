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

export function getAllUserNames() {
  return request({
    url: 'admin/user/name',
    method: 'get'
  })
}
