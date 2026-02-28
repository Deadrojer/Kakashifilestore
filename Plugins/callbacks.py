import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Message, InputMediaPhoto
from pyrogram.enums import ParseMode
from Database.database import Seishiro
from config import *

@Client.on_callback_query()
async def settings_callback(client: Client, callback_query):
    user_id = callback_query.from_user.id
    cb_data = callback_query.data

    try:
        if cb_data == "mode_Quality":
            await Seishiro.set_sequence_mode(user_id, "Quality")
            mode = "Quality"
            await callback_query.answer("Sequence mode set to Quality.", show_alert=True)
            
            # Update the message with current mode selection
            current = mode
            kb = InlineKeyboardMarkup([
                [InlineKeyboardButton(f"Qᴜᴀʟɪᴛʏ{' ✅' if current == 'Quality' else ''}", callback_data="mode_Quality"),
                 InlineKeyboardButton(f"Aʟʟ{' ✅' if current == 'All' else ''}", callback_data="mode_All")],
                [InlineKeyboardButton(f"Eᴘɪsᴏᴅᴇ{' ✅' if current == 'Episode' else ''}", callback_data="mode_Episode"),
                 InlineKeyboardButton(f"Sᴇᴀsᴏɴ{' ✅' if current == 'Season' else ''}", callback_data="mode_Season")]
            ])
            
            await callback_query.message.edit_text(
                f"<b><u>Sᴇʟᴇᴄᴛ Sᴏʀᴛɪɴɢ Mᴏᴅᴇ (Cᴜʀʀᴇɴᴛ: {current})</u></b>: \n\n"
                f"<b><i>• Qᴜᴀʟɪᴛʏ: Sᴏʀᴛ ʙʏ ǫᴜᴀʟɪᴛʏ ᴏɴʟʏ. \n"
                f"• Aʟʟ: Sᴏʀᴛ ʙʏ sᴇᴀsᴏɴ, ǫᴜᴀʟɪᴛʏ, ᴇᴘɪsᴏᴅᴇ. \n"
                f"• Eᴘɪsᴏᴅᴇ: Sᴏʀᴛ ʙʏ ᴇᴘɪsᴏᴅᴇ ᴏɴʟʏ. \n"
                f"• Sᴇᴀsᴏɴ: Sᴏʀᴛ ʙʏ sᴇᴀsᴏɴ ᴏɴʟʏ.</i></b>",
                reply_markup=kb,
                parse_mode=ParseMode.HTML
            )

        elif cb_data == "mode_Episode":
            await Seishiro.set_sequence_mode(user_id, "Episode")
            mode = "Episode"
            await callback_query.answer("Sequence mode set to Episode.", show_alert=True)
            
            current = mode
            kb = InlineKeyboardMarkup([
                [InlineKeyboardButton(f"Qᴜᴀʟɪᴛʏ{' ✅' if current == 'Quality' else ''}", callback_data="mode_Quality"),
                 InlineKeyboardButton(f"Aʟʟ{' ✅' if current == 'All' else ''}", callback_data="mode_All")],
                [InlineKeyboardButton(f"Eᴘɪsᴏᴅᴇ{' ✅' if current == 'Episode' else ''}", callback_data="mode_Episode"),
                 InlineKeyboardButton(f"Sᴇᴀsᴏɴ{' ✅' if current == 'Season' else ''}", callback_data="mode_Season")]
            ])
            
            await callback_query.message.edit_text(
                f"<b><u>Sᴇʟᴇᴄᴛ Sᴏʀᴛɪɴɢ Mᴏᴅᴇ (Cᴜʀʀᴇɴᴛ: {current})</u></b>: \n\n"
                f"<b><i>• Qᴜᴀʟɪᴛʏ: Sᴏʀᴛ ʙʏ ǫᴜᴀʟɪᴛʏ ᴏɴʟʏ. \n"
                f"• Aʟʟ: Sᴏʀᴛ ʙʏ sᴇᴀsᴏɴ, ǫᴜᴀʟɪᴛʏ, ᴇᴘɪsᴏᴅᴇ. \n"
                f"• Eᴘɪsᴏᴅᴇ: Sᴏʀᴛ ʙʏ ᴇᴘɪsᴏᴅᴇ ᴏɴʟʏ. \n"
                f"• Sᴇᴀsᴏɴ: Sᴏʀᴛ ʙʏ sᴇᴀsᴏɴ ᴏɴʟʏ.</i></b>",
                reply_markup=kb,
                parse_mode=ParseMode.HTML
            )

        elif cb_data == "mode_Season":
            await Seishiro.set_sequence_mode(user_id, "Season")
            mode = "Season"
            await callback_query.answer("Sequence mode set to Season.", show_alert=True)
            
            current = mode
            kb = InlineKeyboardMarkup([
                [InlineKeyboardButton(f"Qᴜᴀʟɪᴛʏ{' ✅' if current == 'Quality' else ''}", callback_data="mode_Quality"),
                 InlineKeyboardButton(f"Aʟʟ{' ✅' if current == 'All' else ''}", callback_data="mode_All")],
                [InlineKeyboardButton(f"Eᴘɪsᴏᴅᴇ{' ✅' if current == 'Episode' else ''}", callback_data="mode_Episode"),
                 InlineKeyboardButton(f"Sᴇᴀsᴏɴ{' ✅' if current == 'Season' else ''}", callback_data="mode_Season")]
            ])
            
            await callback_query.message.edit_text(
                f"<b><u>Sᴇʟᴇᴄᴛ Sᴏʀᴛɪɴɢ Mᴏᴅᴇ (Cᴜʀʀᴇɴᴛ: {current})</u></b>: \n\n"
                f"<b><i>• Qᴜᴀʟɪᴛʏ: Sᴏʀᴛ ʙʏ ǫᴜᴀʟɪᴛʏ ᴏɴʟʏ. \n"
                f"• Aʟʟ: Sᴏʀᴛ ʙʏ sᴇᴀsᴏɴ, ǫᴜᴀʟɪᴛʏ, ᴇᴘɪsᴏᴅᴇ. \n"
                f"• Eᴘɪsᴏᴅᴇ: Sᴏʀᴛ ʙʏ ᴇᴘɪsᴏᴅᴇ ᴏɴʟʏ. \n"
                f"• Sᴇᴀsᴏɴ: Sᴏʀᴛ ʙʏ sᴇᴀsᴏɴ ᴏɴʟʏ.</i></b>",
                reply_markup=kb,
                parse_mode=ParseMode.HTML
            )

        elif cb_data == "mode_All":
            await Seishiro.set_sequence_mode(user_id, "All")
            mode = "All"
            await callback_query.answer("Sequence mode set to All (season, episode, quality).", show_alert=True)
            
            current = mode
            kb = InlineKeyboardMarkup([
                [InlineKeyboardButton(f"Qᴜᴀʟɪᴛʏ{' ✅' if current == 'Quality' else ''}", callback_data="mode_Quality"),
                 InlineKeyboardButton(f"Aʟʟ{' ✅' if current == 'All' else ''}", callback_data="mode_All")],
                [InlineKeyboardButton(f"Eᴘɪsᴏᴅᴇ{' ✅' if current == 'Episode' else ''}", callback_data="mode_Episode"),
                 InlineKeyboardButton(f"Sᴇᴀsᴏɴ{' ✅' if current == 'Season' else ''}", callback_data="mode_Season")]
            ])
            
            await callback_query.message.edit_text(
                f"<b><u>Sᴇʟᴇᴄᴛ Sᴏʀᴛɪɴɢ Mᴏᴅᴇ (Cᴜʀʀᴇɴᴛ: {current})</u></b>: \n\n"
                f"<b><i>• Qᴜᴀʟɪᴛʏ: Sᴏʀᴛ ʙʏ ǫᴜᴀʟɪᴛʏ ᴏɴʟʏ. \n"
                f"• Aʟʟ: Sᴏʀᴛ ʙʏ sᴇᴀsᴏɴ, ǫᴜᴀʟɪᴛʏ, ᴇᴘɪsᴏᴅᴇ. \n"
                f"• Eᴘɪsᴏᴅᴇ: Sᴏʀᴛ ʙʏ ᴇᴘɪsᴏᴅᴇ ᴏɴʟʏ. \n"
                f"• Sᴇᴀsᴏɴ: Sᴏʀᴛ ʙʏ sᴇᴀsᴏɴ ᴏɴʟʏ.</i></b>",
                reply_markup=kb,
                parse_mode=ParseMode.HTML
            )
                
        elif cb_data == "about":
            user = await client.get_users(OWNER_ID)
            await callback_query.edit_message_media(
                InputMediaPhoto("https://envs.sh/Wdj.jpg", ABOUT_TXT),
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton("• back", callback_data="start"),
                     InlineKeyboardButton("close •", callback_data="close")]
                ])
            )

        elif cb_data == "help":
            await callback_query.edit_message_media(
                InputMediaPhoto(
                    "https://envs.sh/Wdj.jpg",
                    HELP_TXT.format(
                        first=callback_query.from_user.first_name,
                        last=callback_query.from_user.last_name or "",
                        username=f"@{callback_query.from_user.username}" if callback_query.from_user.username else "None",
                        mention=callback_query.from_user.mention,
                        id=callback_query.from_user.id
                    )
                ),
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton("• back", callback_data="start"),
                     InlineKeyboardButton("close •", callback_data="close")]
                ])
            )

        elif cb_data == "start":
            inline_buttons = InlineKeyboardMarkup([
                [
                    InlineKeyboardButton("• about", callback_data="about"),
                    InlineKeyboardButton("Help •", callback_data="help")
                ]
            ])

            try:
                await callback_query.edit_message_media(
                    InputMediaPhoto(
                        START_PIC,
                        START_MSG.format(
                            first=callback_query.from_user.first_name,
                            last=callback_query.from_user.last_name or "",
                            username=f"@{callback_query.from_user.username}" if callback_query.from_user.username else "None",
                            mention=callback_query.from_user.mention,
                            id=callback_query.from_user.id
                        )
                    ),
                    reply_markup=inline_buttons
                )
            except Exception as e:
                print(f"Error sending start/home photo: {e}")
                await callback_query.edit_message_text(
                    START_MSG.format(
                        first=callback_query.from_user.first_name,
                        last=callback_query.from_user.last_name or "",
                        username=f"@{callback_query.from_user.username}" if callback_query.from_user.username else "None",
                        mention=callback_query.from_user.mention,
                        id=callback_query.from_user.id
                    ),
                    reply_markup=inline_buttons,
                    parse_mode=ParseMode.HTML
                )

        elif cb_data.startswith("rfs_ch_"):
            cid = int(cb_data.split("_")[2])
            try:
                chat = await client.get_chat(cid)
                mode = await Seishiro.get_channel_mode(cid)
                status = "ON" if mode == "on" else "OFF"
                new_mode = "off" if mode == "on" else "on"
                buttons = [
                    [InlineKeyboardButton(f"ForceSub Mode {'OFF' if mode == 'on' else 'ON'}",
                                          callback_data=f"rfs_toggle_{cid}_{new_mode}")],
                    [InlineKeyboardButton("back", callback_data="fsub_back")]
                ]
                await callback_query.message.edit_text(
                    f"Channel: {chat.title}\nCurrent Force-Sub Mode: {status}",
                    reply_markup=InlineKeyboardMarkup(buttons)
                )
            except Exception:
                await callback_query.answer("Failed to fetch channel info", show_alert=True)

        elif cb_data.startswith("rfs_toggle_"):
            parts = cb_data.split("_")[2:]
            cid = int(parts[0])
            action = parts[1]
            mode = "on" if action == "on" else "off"

            await Seishiro.set_channel_mode(cid, mode)
            await callback_query.answer(f"Force-Sub set to {'ON' if mode == 'on' else 'OFF'}")

            chat = await client.get_chat(cid)
            status = "ON" if mode == "on" else "OFF"
            new_mode = "off" if mode == "on" else "on"
            buttons = [
                [InlineKeyboardButton(f"ForceSub Mode {'OFF' if mode == 'on' else 'ON'}",
                                      callback_data=f"rfs_toggle_{cid}_{new_mode}")],
                [InlineKeyboardButton("back", callback_data="fsub_back")]
            ]
            await callback_query.message.edit_text(
                f"Channel: {chat.title}\nCurrent Force-Sub Mode: {status}",
                reply_markup=InlineKeyboardMarkup(buttons)
            )

        elif cb_data == "fsub_back":
            channels = await Seishiro.show_channels()
            buttons = []
            for cid in channels:
                try:
                    chat = await client.get_chat(cid)
                    mode = await Seishiro.get_channel_mode(cid)
                    status = "✅" if mode == "on" else "❌"
                    buttons.append([InlineKeyboardButton(f"{status} {chat.title}", callback_data=f"rfs_ch_{cid}")])
                except Exception:
                    continue

            if not buttons:
                buttons.append([InlineKeyboardButton("No Channels Found", callback_data="no_channels")])

            await callback_query.message.edit_text(
                "Select a channel to toggle its force-sub mode:",
                reply_markup=InlineKeyboardMarkup(buttons + [
                    [InlineKeyboardButton("Close", callback_data="close")]
                ])
            )

        elif cb_data == "close":
            await callback_query.message.delete()
            try:
                await callback_query.message.reply_to_message.delete()
            except:
                pass

    except Exception as e:
        print(f"Error in callback handler: {e}")
        await callback_query.answer("An error occurred. Please try again.", show_alert=True)
