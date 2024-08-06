﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Common.Attributes
{
    [AttributeUsage(AttributeTargets.Field)]
    public class EnumMessageAttribute: Attribute
    {
        public EnumMessageAttribute(string value)
        {
            Value = value;
        }
        public string Value { get; set; }
    }
}