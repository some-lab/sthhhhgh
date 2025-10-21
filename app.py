#!/usr/bin/env python3
# =============================================================================
# app.py — minimal AAA features only (Render-ready: only token in env)
# =============================================================================

import io, os, os.path as op, json, asyncio, random, datetime as dt, typing as t, urllib.parse, uuid, re
import discord
from discord import app_commands
from discord.ext import commands

# ========================== CONFIG ==========================
DISCORD_TOKEN = os.environ["DISCORD_TOKEN"]  # REQUIRED

GUILD_ID                 = "1270144230525763697"
EPHEMERAL                = True
DATA_PATH                = "bot_data.json"

# --- Logging / Admin ---
LOG_CHANNEL_ID           = "1418651467736420402"
ADMIN_ROLE_ID            = "1418651226865799228"

# --- Temp Voice Channels ---
TEMP_VC_HUB_ID           = "1418651399679381626"
TEMP_VC_CATEGORY_ID      = "1418651380834504765"

# --- Invite tracker ---
INVITE_TRACK_CHANNEL_ID  = "1418651401042530496"

# --- Tickets ---
TICKET_CATEGORY_ID       = "1418651387071561871"
TICKET_PANEL_CHANNEL_ID  = "1418651459502739577"

# --- Giveaways ---
GIVEAWAY_CHANNEL_ID      = "1418651444567081122"

# --- Levels ---
LEVEL_ANNOUNCE_CHANNEL_ID = "1418651426007158935"
ROLE_L10   = 1270164309602865315
ROLE_L15   = 1270164755927138384
ROLE_L20   = 1270164954154270731
ROLE_L25   = 1270165116712652860
ROLE_L50   = 1270165259004678165

# --- Counting game ---
COUNTING_CHANNEL_ID      = "1418651415596761232"

# --- Self roles panel ---
SELFROLES_CHANNEL_ID     = "1418651397414719610"

# --- Self roles groups and options ---
ORIGIN_PARENT            = 1418651296923254919
ORIGIN_OPTIONS = {
    "Antarctica": 1418651306100391956,
    "South America": 1418651304464744611,
    "North America": 1418651303818825918,
    "Eurasia": 1418651302506008667,
    "Europe": 1418651301616681020,
    "Australia": 1418651300555391147,
    "Asia": 1418651299418865826,
}

PLATFORM_PARENT          = 1418651313163731147
PLATFORM_OPTIONS = {
    "Mobile Phone": 1418651314098798692,
    "Computer": 1418651315185385632,
    "Playstation": 1418651316670169240,
    "Xbox": 1418651317534199929,
    "Nitendo": 1418651318356283412,
}

GENDER_PARENT            = 1418651291566997696
GENDER_OPTIONS = {
    "Male": 1418651293840576562,
    "Female": 1418651295031628061,
    "Transgender": 1418651295908106311,
}

ABOUT_PARENT             = 1418651286395683007
ABOUT_OPTIONS = {
    "12-14 Years Old": 1418651288899682404,
    "15-17 Years Old": 1418651289814044714,
    "18+ Years Old": 1418651291072073809,
}

# ========================= REST OF BOT BELOW =========================
# (keep full app logic unchanged)
