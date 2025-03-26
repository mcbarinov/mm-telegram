import pytest

from mm_telegram import async_send_message, send_message


def test_send_message_short_message(telegram_token, telegram_chat_id):
    res = send_message(telegram_token, telegram_chat_id, "bla")
    assert len(res.unwrap()) == 1


@pytest.mark.asyncio
async def test_async_send_message_short_message(telegram_token, telegram_chat_id):
    res = await async_send_message(telegram_token, telegram_chat_id, "bla")
    assert len(res.unwrap()) == 1


def test_send_message_long_message(telegram_token, telegram_chat_id):
    message = ""
    for i in range(1800):
        message += f"{i} "
    res = send_message(telegram_token, telegram_chat_id, message)
    assert len(res.unwrap()) == 2


@pytest.mark.asyncio
async def test_async_send_message_long_message(telegram_token, telegram_chat_id):
    message = ""
    for i in range(1800):
        message += f"{i} "
    res = await async_send_message(telegram_token, telegram_chat_id, message)
    assert len(res.unwrap()) == 2
