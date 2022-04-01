local set = vim.opt

-- set.shell = "/bin/sh"
local set = vim.opt
local opt = vim.opt -- global/buffer/windows-scoped options
local cmd = vim.cmd -- execute Vim commands

set.expandtab = true
set.smarttab = true
set.shiftwidth = 4
set.tabstop = 4

set.hlsearch = false
set.incsearch = true
set.ignorecase = true
set.smartcase = true

set.termguicolors = true
set.showmode = false
set.splitbelow = true
set.splitright = true
set.wrap = false
set.breakindent = true
set.scrolloff = 5
set.fileencoding = "utf-8"
set.conceallevel = 2

set.relativenumber = true
set.number = true
-- set.cursorline = true
set.wildmenu = true
set.completeopt = "menuone,noselect"

set.hidden = true
set.mouse = "a"

vim.cmd([[colorscheme gruvbox]])

-- remove whitespace on save
cmd([[au BufWritePre * :%s/\s\+$//e]])

-- don't auto commenting new lines
cmd([[au BufEnter * set fo-=c fo-=r fo-=o]])
