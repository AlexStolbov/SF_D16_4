# Представьте, что у вас есть приложение, которое оптимизировано как для ПК,
# так и для мобильных устройств. Шаблоны для этих версий хранятся
# в каталогах full/ и mobile/. Гарантируется, что состав шаблонов идентичен,
# отличается лишь содержание.
# Создайте простой middleware, который будет отправлять пользователю
# соответствующую версию.

import logging


class SelectTemplate:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # код, выполняемый до формирования ответа (или другого middleware)

        response = self.get_response(request)

        # код, выполняемый после формирования запроса (или нижнего слоя)

        # решение платформы
        # if request.mobile:
        if 1:
            response.template_name = 'full/maker_list.html'
        else:
            response.template_name = 'mobile/maker_list.html'

        # test logging system
        logger = logging.getLogger('django')
        # logger.debug('(deb) from call')
        logger.warning('----------------------------- (warn) from call')
        logger.error('------------------------------- (error) from call')
        logger.critical('--------------------------- (critical) from call')
        logger_req = logging.getLogger('django.request')
        logger_req.error('>>>> from call')
        #

        return response

    # мое решение
    # def process_template_response(self, request, response):
    #     print(f'request: {request}')
    #     if request.mobile:
    #         response.template_name = 'full/maker_list.html'
    #     else:
    #         response.template_name = 'mobile/maker_list.html'
    #
    #     return response
