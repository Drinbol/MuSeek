export interface Material {
    id: number;
    content: string;
    tags: Tag[];
  }
  
export interface Tag {
  id: number;
  name: string;
  type: string;
}