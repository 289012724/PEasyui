# -*- coding: utf-8 -*- 
# @file: tag.py
# @purpose: a HTML tag generator
# @author: MicoMeter <289012724@qq.com>

__doc__         = """
@attention:The Tag.py module is the core of the PyH package. Tag lets you
generate HTML tags from within your python code.
See https://github.com/289012724 for documentation.
@param _attributies: use to contain all properties,such as id,width,height and so on 
@param _children   : use to contain all child node
@param _tagName    : the name of the tag,defualt value is "div"
@param _lib        : other render libary,which can add or modify the object _attributies,
such as easyui,bootstrap
"""

__author__      = "MicoMeter <289012724@qq.com>"
__version__     = '$Revision$'
__date__        = '$Date$'

import copy
_tag_attr   = ["_attributies","_children","_tagName","_lib"]

class tag(object):
    def __init__(self,**kwargs):
        object.__init__(self,**kwargs)
        self._attributies   = kwargs
        self._children      = kwargs.get("child")or []
        self._tagName       = kwargs.get("name") or "div"
        self._lib           = kwargs.get("lib")  or []

    def attr(self,**kwargs):self._attributies.update(kwargs)
    def append(self,*args):self._children.extend(args)
    def appendTo(self,*args):[_arg.append(self) for _arg in args]
    def clone(self):return copy.deepcopy(self)

    def hasChildren(self):return len(self._children)>0

    def _get_attributies(self):
        _att = '%s="%s"'
        _atts= []
        def _get_key(key):
            if key not in ["text","cls"]:
                if key=="cls":key="class"
                return key

        for key,value in self._attributies.iteritems():
            key=_get_key(key)
            if key:_atts.append(_att%(key,value))
        _atts.reverse()
        return _atts

    def _get_text(self):return self._attributies.get("text") or ""

    def _render_lib(self):[_lib,render(self) for _lib in self._lib]

    def _render_current(self,obj):
        obj._render_lib()
        _text=self._get_text()
        _atts=self._get_attributies()
        string="<%s %s>%s"%(self._tagName," ".join(_atts),_text)
        return string

    def _render_one(self,obj):
        string = self._render_current(obj)+"\n"
        for _c in obj._children:
            string +=_c.render()
        string +="</%s>"%self._tagName
        return string

    def render(self):
        string = self._render_one(self)
        return string+"\n"

    def __get__(self,key):
        if hasattr(self,key):return self.__dict__.get(key)
        else:return self._attributies.get(key)

    def __setattr__(self,key,value):
        if key in _tag_attr:self.__dict__[key]=value
        else: self._attributies[key]=value

    def __delattr__(self,key):
        if key not in _tag_attr and self._attributies.has_key(key):
            return self._attributies.pop(key)
        raise KeyError,"input property is wrong:%s"%key












