# FastAPI-Svelte-YoloV5

Simple detect items web use FastAPI framework in back-end and Svelte framework in front-end.

![Screenshot](https://raw.githubusercontent.com/Nguyen-Hoang-Nam/readme-image/main/fastapi-svelte-yolov5/screenshot.png)

## Usage

Put your `YoloV5` or `YoloV3` weight in `backend/model/` and change path in `backend/model/yolov5.py`.

```bash
$ cd backend
$ uvicorn main:app --reload
$ cd ../fronend
$ npm run dev
```

## Todo

- [ ] Upload weight
- [ ] Test multiple image

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
