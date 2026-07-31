export interface DatasetInfo {
  filename: string;
  rows: number;
  columns: number;
  column_names: string[];
  preview: Record<string, any>[];
}