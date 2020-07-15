import request from '@/utils/request'

export function loginByUsername(username, password) {
  const data = {
    username,
    password
  }
  return request({
    url: '/api/login',
    method: 'post',
    data
  })
}

export function logout() {
  return request({
    url: '/api/logout',
    method: 'get'
  })
}

export function register(data) {
  return request({
    url: '/api/regist',
    method: 'post',
    data
  })
}

export function resetpassword(data) {
  return request({
    url: '/api/resetpassword',
    method: 'post',
    data
  })
}
