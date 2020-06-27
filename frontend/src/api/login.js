import request from '@/utils/request'

export function loginByUsername(username, password) {
  const data = {
    username,
    password
  }
  return request({
    url: '/login',
    method: 'post',
    data
  })
}

export function logout() {
  return request({
    url: '/logout',
    method: 'get'
  })
}

export function register(data) {
  return request({
    url: '/regist',
    method: 'post',
    data
  })
}

export function resetpassword(data) {
  return request({
    url: '/resetpassword',
    method: 'post',
    data
  })
}
