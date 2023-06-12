import Axios, { AxiosRequestConfig } from 'axios';

const API_HOST = 'http://localhost:9000';

export const AXIOS = Axios.create({
  baseURL: API_HOST,
  headers: {
    accept: 'application/json',
  },
});