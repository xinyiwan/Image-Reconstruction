from skimage.metrics import peak_signal_noise_ratio
from skimage.metrics import structural_similarity as ssim
from skimage.metrics import mean_squared_error

def evaluate(img,img_recon):
    img = (img - img.min())/(img.max() - img.min())*255
    img_recon = (img_recon - img_recon.min())/(img_recon.max() - img_recon.min())*255

    psnr = peak_signal_noise_ratio(img,abs(img_recon),data_range=img.max()-img.min())
    ssim_value = ssim(img, img_recon, data_range=img_recon.max()-img_recon.min())
    mse = mean_squared_error(img, abs(img_recon))
    print("PSNR = {}".format(psnr))
    print("SSIM = {}".format(ssim_value))
    print("MSE = {}".format(mse))
    print(" ")