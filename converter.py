def v3_to_v1(payload: dict|list, create_or_update: str):
    if type(payload) == dict:
        props = [{"property":k, "value":v} for k, v in payload["properties"].items()]
        properties = {"properties":props}
        return properties
    elif type(payload) == list:
        lst = []
        for record in payload:
            props = []
            for k, v in record["properties"].items():
                props.append({"property":k, "value":v})
            if create_or_update == "update":
                properties["vid"] = record["id"]
            lst.append({"properties":props})
        return lst

def v1_to_v3(payload, create_or_update: str):
    if type(payload) == dict:
        props = {}
        for properties in payload["properties"]:
            props[properties["property"]] = properties["value"] 
        properties = {"properties":props}
        return properties

    elif type(payload) == list:
        lst = []
        for record in payload:
            props = {}
            for properties in record["properties"]:
                props[properties["property"]] = properties["value"] 
            properties = {"properties":props}
            if create_or_update == "update":
                properties["id"] = record["vid"]
            lst.append(props)
        return lst