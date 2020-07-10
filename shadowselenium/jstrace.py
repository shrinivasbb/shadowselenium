

class JSTrace:

    js_one_element='''let findShadowElement=(()=>{
                    return document.querySelector('param1').shadowRoot.querySelector('param2');
                    });
                    return findShadowElement()'''

    js_one_webelement = '''let findShadowElement=(()=>{
                    return arguments[0].shadowRoot.querySelector('param2');
                    });
                    return findShadowElement()'''

    js_all_elements='''let findShadowElement=(()=>{
                    return document.querySelector('param1').shadowRoot.querySelectorAll('param2');
                    });
                    return findShadowElement()'''

    js_all_webelement = '''let findShadowElement=(()=>{
                    return arguments[0].shadowRoot.querySelectorAll('param2');
                    });
                    return findShadowElement()'''

