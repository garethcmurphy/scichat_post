#!/usr/bin/env python3
"""kafa consume"""
import json
from kafka import KafkaConsumer, TopicPartition


def main():
    """setup consumer"""
    consumer = KafkaConsumer(
        bootstrap_servers=['localhost:9093'],
        enable_auto_commit=False,
        value_deserializer=lambda x: json.loads(x.decode('utf-8')))
    partition = TopicPartition('V20_writerCommand', 0)
    consumer.seek(partition=partition, offset=1210)

    for message in consumer:
        # message value and key are raw bytes -- decode if necessary!
        # e.g., for unicode: `message.value.decode('utf-8')`
        print("%s:%d:%d: key=%s value=" % (message.topic, message.partition,
                                           message.offset, message.key
                                           ))
        if "cmd" in message.value:
            print(message.value["cmd"])


if __name__ == "__main__":
    main()
