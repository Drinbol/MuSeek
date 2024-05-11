import axios from 'axios';
import type { Material, Tag } from '../types';

// 创建一个 axios 实例
const instance = axios.create({
  baseURL: 'http://192.168.0.101:8000', // 将此处替换为你的后端服务器的实际地址
});

export async function listMaterials() {
  const res = await instance.get<Material[]>('/materials');
  return res.data;
}

export async function getMaterial(id: number) {
  const res = await instance.get<Material>(`/materials/${id}`);
  return res.data;
}

export async function createMaterial(data: { content: string; tag_ids: number[] }) {
  const res = await instance.post<Material>('/materials', data);
  return res.data;
}
export async function updateMaterial(id: number, data: Partial<Material>) {
  const res = await instance.put<Material>(`/materials/${id}`, data);
  return res.data;
}

export async function deleteMaterial(id: number) {
  await instance.delete(`/materials/${id}`);
}

export async function listTags() {
  const res = await instance.get<Tag[]>('/tags');
  return res.data;
}