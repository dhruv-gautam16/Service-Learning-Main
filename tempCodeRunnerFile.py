    """Returns a list of detection results, each a dictionary of object info."""
        set_input_tensor(interpreter, image)
        interpreter.invoke()
        # Get all output details
        boxes = get_output_tensor(interpreter, 0)
        classes = get_output_tensor(interpreter, 1)
        scores = get_output_tensor(interpreter, 2)
        count = int(get_output_tensor(interpreter, 3))

        results = []
        for i in range(count):
            if scores[i] >= threshold:
            result = {
                'bounding_box': boxes[i],
                'class_id': classes[i],
                'score': scores[i]
            }
            results.append(result)
        return results