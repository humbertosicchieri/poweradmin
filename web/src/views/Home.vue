<template>
  <div class="space-y-12">
    <!-- Hero Section -->
    <section class="text-center space-y-6 py-16">
      <h1 class="text-5xl md:text-6xl font-bold bg-gradient-to-r from-blue-400 to-cyan-400 bg-clip-text text-transparent">
        PowerAdmin
      </h1>
      <p class="text-xl text-slate-300 max-w-3xl mx-auto">
        Repositório profissional de scripts Microsoft para PowerShell, Batch e VBScript. Automação inteligente com IA e sincronização em tempo real via N8N.
      </p>
      <div class="flex flex-col sm:flex-row gap-4 justify-center">
        <router-link to="/scripts" class="px-8 py-3 bg-gradient-to-r from-blue-600 to-cyan-600 rounded-lg font-semibold hover:shadow-lg hover:shadow-blue-500/50 transition">
          Explorar Scripts
        </router-link>
        <a href="https://github.com/humbertosicchieri/poweradmin" target="_blank" class="px-8 py-3 border border-slate-600 rounded-lg font-semibold hover:bg-slate-800 transition">
          Ver no GitHub
        </a>
      </div>
    </section>

    <!-- Stats -->
    <section class="grid grid-cols-1 md:grid-cols-3 gap-6">
      <div class="bg-slate-800/50 border border-slate-700 rounded-lg p-6 text-center hover:border-blue-500 transition">
        <div class="text-4xl font-bold text-blue-400">{{ stats.scripts }}</div>
        <div class="text-slate-400 mt-2">Scripts Disponíveis</div>
      </div>
      <div class="bg-slate-800/50 border border-slate-700 rounded-lg p-6 text-center hover:border-cyan-500 transition">
        <div class="text-4xl font-bold text-cyan-400">{{ stats.categories }}</div>
        <div class="text-slate-400 mt-2">Categorias</div>
      </div>
      <div class="bg-slate-800/50 border border-slate-700 rounded-lg p-6 text-center hover:border-purple-500 transition">
        <div class="text-4xl font-bold text-purple-400">{{ stats.updated }}</div>
        <div class="text-slate-400 mt-2">Sincronizações/Dia</div>
      </div>
    </section>

    <!-- Categories -->
    <section class="space-y-6">
      <h2 class="text-3xl font-bold">Categorias Principais</h2>
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
        <router-link 
          v-for="cat in categories" 
          :key="cat.id" 
          to="/scripts"
          :query="{ category: cat.name }"
          class="bg-slate-800/50 border border-slate-700 hover:border-blue-500 rounded-lg p-6 cursor-pointer transition hover:bg-slate-800/80"
        >
          <div class="text-4xl mb-3">{{ cat.icon }}</div>
          <h3 class="font-semibold mb-2">{{ cat.name }}</h3>
          <p class="text-sm text-slate-400">{{ cat.count }} scripts</p>
        </router-link>
      </div>
    </section>

    <!-- Features -->
    <section class="space-y-6">
      <h2 class="text-3xl font-bold">Recursos</h2>
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <div class="bg-slate-800/50 border border-slate-700 rounded-lg p-6">
          <div class="text-3xl mb-3">🔄</div>
          <h3 class="font-semibold mb-2">Sincronização Automática</h3>
          <p class="text-slate-400 text-sm">Scripts sincronizados automaticamente do GitHub via N8N</p>
        </div>
        <div class="bg-slate-800/50 border border-slate-700 rounded-lg p-6">
          <div class="text-3xl mb-3">🤖</div>
          <h3 class="font-semibold mb-2">Categorização com IA</h3>
          <p class="text-slate-400 text-sm">Classificação automática de scripts por tipo e categoria</p>
        </div>
        <div class="bg-slate-800/50 border border-slate-700 rounded-lg p-6">
          <div class="text-3xl mb-3">🐳</div>
          <h3 class="font-semibold mb-2">Deploy em Docker</h3>
          <p class="text-slate-400 text-sm">Infraestrutura completa em containers Docker Compose</p>
        </div>
        <div class="bg-slate-800/50 border border-slate-700 rounded-lg p-6">
          <div class="text-3xl mb-3">⚡</div>
          <h3 class="font-semibold mb-2">Performance</h3>
          <p class="text-slate-400 text-sm">Interface responsiva construída com Vue 3 + Vite</p>
        </div>
        <div class="bg-slate-800/50 border border-slate-700 rounded-lg p-6">
          <div class="text-3xl mb-3">🔍</div>
          <h3 class="font-semibold mb-2">Busca Rápida</h3>
          <p class="text-slate-400 text-sm">Encontre scripts por nome, descrição ou categoria</p>
        </div>
        <div class="bg-slate-800/50 border border-slate-700 rounded-lg p-6">
          <div class="text-3xl mb-3">📱</div>
          <h3 class="font-semibold mb-2">Responsivo</h3>
          <p class="text-slate-400 text-sm">Funciona perfeitamente em desktop, tablet e mobile</p>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const stats = ref({
  scripts: 156,
  categories: 8,
  updated: '24/7'
})

const categories = ref([
  { id: 1, name: 'Active Directory', icon: '👥', count: 28 },
  { id: 2, name: 'Exchange', icon: '📧', count: 19 },
  { id: 3, name: 'SQL Server', icon: '🗄️', count: 22 },
  { id: 4, name: 'Windows Server', icon: '🖥️', count: 31 },
  { id: 5, name: 'Hyper-V', icon: '☁️', count: 15 },
  { id: 6, name: 'Backup', icon: '💾', count: 18 },
  { id: 7, name: 'Network', icon: '🌐', count: 12 },
  { id: 8, name: 'Security', icon: '🔒', count: 14 }
])
</script>
