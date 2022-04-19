return require("packer").startup(function()
    use("wbthomason/packer.nvim") --> packer plugin manager

    -->
    use("kyazdani42/nvim-web-devicons") --> enable icons
    use("norcalli/nvim-colorizer.lua")
    use("nvim-lualine/lualine.nvim") --> a statusline written in lua
    use("romgrk/barbar.nvim") --> tabs for neovim
    use("kyazdani42/nvim-tree.lua") --> file explorer
    use("akinsho/toggleterm.nvim")
    use("nvim-lua/plenary.nvim")
    use("nvim-telescope/telescope.nvim") --> Find, Filter, Preview, Pick. All lua, all the time.
    use("numToStr/Comment.nvim")
    use("ggandor/lightspeed.nvim") --> motion plugin with incremental input processing, allowing for unparalleled speed with near-zero cognitive effort
    use("windwp/nvim-autopairs")
    use("windwp/nvim-ts-autotag")

    use("sunjon/shade.nvim") --> dim inactive windows
    use({ "folke/which-key.nvim" })
    use("mhartington/formatter.nvim") --> dim inactive windows

    --> colorschemes
    use("ellisonleao/gruvbox.nvim")

    use("nvim-neorg/neorg")
    --> Markdwon preview
    use({
        "iamcco/markdown-preview.nvim",
        ft = "markdown",
        run = "cd app && yarn install",
    })

    --> treesitter & treesitter modules/plugins
    use({ "nvim-treesitter/nvim-treesitter", run = ":TSUpdate" }) --> treesitter
    use("nvim-treesitter/nvim-treesitter-textobjects") --> textobjects
    use("nvim-treesitter/nvim-treesitter-refactor")
    use("p00f/nvim-ts-rainbow")
    use("nvim-treesitter/playground")
    use("JoosepAlviste/nvim-ts-context-commentstring")

    --> lsp
    use("neovim/nvim-lspconfig") --> Collection of configurations for built-in LSP client
    use("williamboman/nvim-lsp-installer") --> Companion plugin for lsp-config, allows us to seamlesly install language servers
    use("jose-elias-alvarez/null-ls.nvim") --> inject lsp diagnistocs, formattings, code actions, and more ...
    use("tami5/lspsaga.nvim") --> icons for LSP diagnostics
    use("onsails/lspkind-nvim") --> vscode-like pictograms for neovim lsp completion items
    use("hrsh7th/nvim-cmp") --> Autocompletion plugin
    use({ "hrsh7th/cmp-buffer" })

    use("hrsh7th/cmp-nvim-lsp") --> LSP source for nvim-cmp
    use("saadparwaiz1/cmp_luasnip") --> Snippets source for nvim-cmp
    use("L3MON4D3/LuaSnip") --> Snippets plugin
    use("WhoIsSethDaniel/toggle-lsp-diagnostics.nvim") --> toggle diagnostics
    use("rafamadriz/friendly-snippets") -- a bunch of snippets to use

    --> Neovim statup
    use({ "glepnir/dashboard-nvim" })
end)
