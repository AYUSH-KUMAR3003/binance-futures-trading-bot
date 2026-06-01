import click
from bot.client import get_client
from bot.orders import (
    place_market_order,
    place_limit_order
)
from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity
)
from bot.logging_config import logger


@click.command()

@click.option(
    "--symbol",
    required=True,
    help="Trading pair (e.g. BTCUSDT)"
)

@click.option(
    "--side",
    required=True,
    help="BUY or SELL"
)

@click.option(
    "--order_type",
    required=True,
    help="MARKET or LIMIT"
)

@click.option(
    "--quantity",
    required=True,
    help="Order quantity"
)

@click.option(
    "--price",
    required=False,
    help="Required for LIMIT orders"
)

def main(
    symbol,
    side,
    order_type,
    quantity,
    price
):

    try:

        # Validation
        validate_side(side)
        validate_order_type(order_type)
        validate_quantity(quantity)

        logger.info(
            f"Order Request: "
            f"{symbol}, {side}, "
            f"{order_type}, {quantity}, {price}"
        )

        client = get_client()

        print("\n===== ORDER REQUEST SUMMARY =====")

        print(f"Symbol       : {symbol}")
        print(f"Side         : {side}")
        print(f"Order Type   : {order_type}")
        print(f"Quantity     : {quantity}")

        if price:
            print(f"Price        : {price}")

        # MARKET ORDER
        if order_type.upper() == "MARKET":

            response = place_market_order(
                client,
                symbol,
                side,
                quantity
            )

        # LIMIT ORDER
        else:

            if not price:
                raise ValueError(
                    "Price is required for LIMIT order"
                )

            response = place_limit_order(
                client,
                symbol,
                side,
                quantity,
                price
            )

        logger.info(
            f"Order Response: {response}"
        )

        print("\n===== ORDER RESPONSE =====")

        print(
            f"Order ID     : {response.get('orderId')}"
        )

        print(
            f"Status       : {response.get('status')}"
        )

        print(
            f"Executed Qty : {response.get('executedQty')}"
        )

        print(
            f"Avg Price    : {response.get('avgPrice')}"
        )

        print(
            "\nSUCCESS: Order submitted successfully."
        )

    except Exception as error:

        logger.error(str(error))

        print(
            f"\nFAILED: {error}"
        )


if __name__ == "__main__":
    main()