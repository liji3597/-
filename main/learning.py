from loguru import logger

def load_checkpoint1(self, ckpt):
    # 加载检查点的逻辑
    logger.info("Successfully loaded checkpoint {}".format(ckpt))
    # 其他加载检查点后的处理逻辑
    return self