import { defineConfig, loadEnv } from 'vite';
import react from '@vitejs/plugin-react';

export default ({ mode }) => {
  const { VITE_PROXY } = loadEnv(mode, process.cwd());

  return defineConfig({
    plugins: [react()],
    build: { outDir: '../backend/templates' },
    base: './',
    server: {
      proxy: {
        '/api': {
          target: VITE_PROXY || 'http://127.0.0.1:5000',
          changeOrigin: true,
        },
      },
    },
  });
};
