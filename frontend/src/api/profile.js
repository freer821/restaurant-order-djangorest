import request from '@/utils/request'

export function changePassword(data) {
  return request({
    url: '/api/user/changepassword',
    method: 'put',
    data
  })
}

export function nNotice() {
  return request({
    url: '/profile/nnotice',
    method: 'get'
  })
}
