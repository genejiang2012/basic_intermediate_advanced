#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
File: controller.py
Author: Gene Jiang
Email: genejiang2012@outlook.com
Github: https://github.com/genejiang2012
Description: 
"""
from design_pattern.greeting_mvc.models import NameModel, TimeModel
from design_pattern.greeting_mvc.view import GreetingView


class GenericController:
    """Docstring for GenericController. """

    def __init__(self):
        """TODO: to be defined1. """
        self.name_model = NameModel()
        self.time_model = TimeModel()
        self.view = GreetingView()

    def handle(self, request):
        if request in self.name_model.get_name_list():
            self.view.generate_greeting(
                name=request,
                known=True,
                time_of_day=self.time_model.get_time_of_day()
            )
        else:
            self.name_model.save_name(request)
            self.view.generate_greeting(
                name=request,
                known=False,
                time_of_day=self.time_model.get_time_of_day()
            )


